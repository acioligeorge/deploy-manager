import { useState,useEffect } from "react"
import type { Deployment } from "./types/deployments"

function App() {
  // ESTADO: dados que o componente guarda e re-renderiza quando mudam
  const [deployments, setDeployments] = useState<Deployment[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // EFEITO: código que faz correr depois que redeniza na interface
  useEffect(() => {
    fetchDeployments()
  }, []);

  async function fetchDeployments() {
    try {
      setLoading(true)
      const res = await fetch ("http://localhost:8001/deployments")
      const data = await res.json()
      setDeployments(data)
    } catch (err) {
      setError("Erro ao carregar os deployments")
    } finally {
      setLoading(false)
    }
  }

    if (loading) return <p>A Carregar...</p>
    if (error) return <p>{error}</p>

    return (
      <div>
        <h1>Deployments</h1>
        <ul>
          {deployments.map((dep) => (
            <li key={dep.id}>{dep.name}, {dep.created_at} - {dep.status}</li>
          ))}
        </ul>
      </div>
    );
  }


  export default App