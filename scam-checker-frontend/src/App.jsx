import { useState } from 'react'
import './App.css'

function App() {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleFileChange = (e) => {
    setFile(e.target.files[0])
    setResult(null) // Reset previous results
    setError(null)
  }

  const checkScam = async (e) => {
    e.preventDefault()
    if (!file) return

    setLoading(true)
    setError(null)

    // Package the image exactly how FastAPI expects it
    const formData = new FormData()
    formData.append("file", file)

    try {
      const response = await fetch("http://localhost:8000/analyze-scam", {
        method: "POST",
        body: formData,
      })

      if (!response.ok) {
        throw new Error("Failed to analyze the image.")
      }

      const data = await response.json()
      // FastAPI returns { id: ..., analysis: { status, category, explanation } }
      setResult(data.analysis) 
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Is This a Scam?</h1>
      <p>Upload a screenshot of a suspicious text or email to check if it's safe.</p>

      <form onSubmit={checkScam}>
        <input 
          type="file" 
          accept="image/*" 
          onChange={handleFileChange} 
        />
        <button type="submit" disabled={!file || loading}>
          {loading ? "Analyzing..." : "Check Screenshot"}
        </button>
      </form>

      {error && <div className="error-box">Error: {error}</div>}

      {result && (
        <div className={`result-box ${result.status.toLowerCase()}`}>
          <h2>Verdict: {result.status}</h2>
          <p><strong>Category:</strong> {result.category}</p>
          <p><strong>Explanation:</strong> {result.explanation}</p>
        </div>
      )}
    </div>
  )
}

export default App