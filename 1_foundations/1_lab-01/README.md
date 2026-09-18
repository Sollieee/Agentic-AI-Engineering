# Lab 1 — First Steps into Agentic AI

## Overview

This lab is my first practical step into Agentic AI.

The goal was to get a working environment set up, make API calls to an LLM, and begin exploring how multiple LLM calls can be connected together to perform a simple multi-step task.

This lab was completed as part of my Agentic AI learning journey, based on **Ed Donner's Agentic AI course**.

## What I Learned

In this lab, I worked with:

- Python environment variables and `.env`
- The OpenAI Python library
- LLM API calls and Message-based prompting
- Passing the output of one LLM call into another
- Using an LLM to generate and evaluate an answer

## What I Built

The notebook starts with a simple LLM interaction and gradually builds toward a multi-step workflow.

The workflow includes:

1. Loading API credentials securely through environment variables.
2. Connecting to an LLM through the OpenAI API.
3. Asking the LLM to identify a potential pain point in agriculture.
4. Asking the LLM to generate a challenging question.
5. Asking another LLM call to answer the question.
6. Exploring a potential Agentic AI application in agriculture.


## My Experimentation

I adapted the exercise toward **agriculture**, connecting the concepts to an area I already understand.


```text
User
  ↓
LLM identifies an agriculture pain point
  ↓
LLM generates a challenging question
  ↓
LLM produces an answer
  ↓
Another LLM evaluates the answer
  ↓
Agentic AI opportunity
