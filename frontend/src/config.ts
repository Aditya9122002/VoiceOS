// Runtime configuration, read once at startup from Vite environment variables.
// A missing value fails immediately with an actionable message, mirroring how the
// backend validates its settings at startup.

function requireEnv(name: keyof ImportMetaEnv): string {
  const value = import.meta.env[name]
  if (!value) {
    throw new Error(`${name} is not set. Copy frontend/.env.example to frontend/.env.`)
  }
  return value
}

export const config = {
  // Trailing slashes are removed so paths can always be joined with a leading "/".
  apiBaseUrl: requireEnv('VITE_API_BASE_URL').replace(/\/+$/, ''),
}
