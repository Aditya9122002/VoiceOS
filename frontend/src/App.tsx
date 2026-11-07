import { useEffect, useState } from 'react'
import { config } from './config'

type BackendStatus = 'checking' | 'ok' | 'unreachable'

// Foundation check only: confirms the frontend can reach the backend with the
// configured URL and that CORS is set up correctly. No product features yet.
export default function App() {
  const [status, setStatus] = useState<BackendStatus>('checking')

  useEffect(() => {
    const controller = new AbortController()

    fetch(`${config.apiBaseUrl}/health`, { signal: controller.signal })
      .then((response) => setStatus(response.ok ? 'ok' : 'unreachable'))
      .catch(() => {
        if (!controller.signal.aborted) setStatus('unreachable')
      })

    return () => controller.abort()
  }, [])

  return (
    <main>
      <h1>VoiceOS</h1>
      <p>Backend status: {status}</p>
    </main>
  )
}
