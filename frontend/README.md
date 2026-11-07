# Frontend

The VoiceOS browser client: React and TypeScript, built with Vite. At this stage it contains only the development foundation and a page that shows whether the backend is reachable. No product features are implemented.

## Requirements

- A Node.js version supported by the installed Vite release (currently `^20.19.0` or `>=22.12.0`).

## Setup

```text
cd frontend
npm install
```

Copy `.env.example` to `.env`. The `.env` file is ignored by git.

Every `VITE_` variable is embedded in the JavaScript sent to the browser and is therefore public. Never put secrets in the frontend environment.

## Run

```text
npm run dev
```

The dev server uses port 5173 and is configured to fail instead of choosing another port if it is taken, because the backend allows cross-origin requests only from that origin (see `backend/.env.example`). Start the backend first for the status line to show `ok`.

## Quality checks

```text
npm run check          # typecheck, lint, and format check together
npm run typecheck      # TypeScript, strict mode
npm run lint           # Oxlint
npm run format:check   # Prettier
npm run format         # apply formatting
npm run build          # production build
```

## Layout

```text
frontend/
├── src/
│   ├── App.tsx       Root component
│   ├── config.ts     Validated runtime configuration
│   ├── env.d.ts      Types for environment variables
│   ├── index.css     Base styles
│   └── main.tsx      Entry point
└── index.html
```
