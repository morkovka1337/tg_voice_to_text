# Telegram Voice To Text

## Architecture Overview
1. Ready Speech to Text model
2. Ready puctuation model for text postprocessing
    1. Ready russian model
    2. Ready english model (if it works)
    3. Finetune english model or train from scratch manually
3. Telegram bot as interface
4. Hosting as models' backend

## Optionally
1. Audio message summarizer.

    We can enter text and get summarized post-processed output.
    Check raw text?

