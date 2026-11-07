// Declares the environment variables this application reads, so that a typo in a
// variable name is a compile error. Only variables prefixed with VITE_ are exposed
// to the browser, which means they are public: never put a secret here.
interface ImportMetaEnv {
  readonly VITE_API_BASE_URL?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
