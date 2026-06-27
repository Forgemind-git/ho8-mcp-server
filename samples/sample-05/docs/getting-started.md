# Getting Started

Welcome to Acme SaaS! This guide walks you through your first setup.

## Step 1: Create an account

Go to https://app.acme.io/signup and enter your email address.
You will receive a confirmation email within a few minutes.

## Step 2: Install the CLI

```bash
pip install acme-cli
acme login
```

## Step 3: Create your first project

```bash
acme project create my-project
```

This creates a new project with default settings.
You can customise settings in `acme.yaml`.

## Step 4: Invite team members

Go to Settings > Team and enter the email addresses of your teammates.
Team members receive an invitation email and can join with one click.

## Troubleshooting

If you see "authentication failed", run `acme logout` then `acme login` again.
If your confirmation email is missing, check your spam folder.
