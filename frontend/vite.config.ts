import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// The backend allows cross-origin requests from this exact origin (see
// backend/.env.example). strictPort makes Vite fail loudly if the port is taken,
// instead of silently moving to another port that the backend would then reject.
const DEV_SERVER_PORT = 5173

export default defineConfig({
  plugins: [react()],
  server: { port: DEV_SERVER_PORT, strictPort: true },
})
