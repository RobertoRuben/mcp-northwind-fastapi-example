# Northwind FastAPI MCP Example

This project demonstrates how to use fastapi-mcp to create a Model Context Protocol (MCP) server that allows Large Language Models (LLMs) to connect and interact with a REST API.

## Overview

The Northwind API is a simple example that shows how to expose data from the classic Northwind database through both a traditional REST API and an MCP endpoint, making it accessible for LLMs to query and understand.

## Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment tool

### Installation

1. Clone the repository and install dependencies:   ```bash
   git clone https://github.com/RobertoRuben/mcp-northwind-fastapi-example.git
   cd mcp-northwind-fastapi-example
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn src.main:app --reload
   ```

3. Access the API documentation at `http://localhost:8000/api/v1/docs`

## Available Endpoints

### REST API Endpoints

- `GET /api/v1/products`: List all products

### MCP Endpoint

- `http://localhost:8000/mcp`: Model Context Protocol endpoint for LLM connections

## Connecting an LLM to the API

This example demonstrates how fastapi-mcp creates a bridge between your REST API and Large Language Models:

1. Traditional REST endpoints serve structured data at `/api/v1/products*`
2. The MCP endpoint at `/mcp` allows LLMs to discover and interact with your API programmatically
3. LLMs can understand your data schema and execute appropriate API calls automatically.
