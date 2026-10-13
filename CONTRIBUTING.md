# Contributing

## Secrets

- Never commit real API keys, tokens or passwords.
- Copy `.env.example` to `.env` and put your own Riot API key there:
  `cp .env.example .env` (Windows: `copy .env.example .env`).
- `.env` is listed in `.gitignore`. Check with `git status` before every commit
  that `.env` does not appear.
- Only put dummy values in `.env.example`.
- If a key was pushed by mistake, tell the team lead and regenerate the key on
  the Riot developer portal immediately. Deleting the commit is not enough.
