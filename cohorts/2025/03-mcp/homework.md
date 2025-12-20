# Model Context Protocol (MCP)

In this homework, we will build our own MCP server - a clone of Context7.

For that, we will need:

- Select a GitHub repo with documentation
- Download the data from it
- Make it searchable

Let's start!


## Question 1: Create a New Project

Create a new project. We will use `uv` for dependency management. Install it if you don't have it:

```bash
pip install uv
```

Create a directory and initialize an empty project there:

```bash
uv init
```

Install fastmcp:

```bash
uv add fastmcp
``` 


In `uv.lock`, what's the first hash in the `wheels` section of `fastmcp`? Include the entire string without quotes.

```
fb3e365cc1d52573ab89caeba9944dd4b056149097be169bce428e011f0a57e5
```

## Question 2: FastMCP Transport

Now let's update the main file.

Use the starter code from [their docs](https://github.com/jlowin/fastmcp):

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```


Run the server.

You'll see the welcome screen. What's the transport?

* **STDIO** (answer) 
* HTTP
* HTTPS
* SSE

```bash
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │
│                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │
│                                                                              │
│                                FastMCP 2.14.1                                │
│                                                                              │
│                                                                              │
│                    🖥  Server name: Demo 🚀                                   │
│                                                                              │
│                    📦 Transport:   STDIO                                     │
│                                                                              │
│                    📚 Docs:        https://gofastmcp.com                     │
│                    🚀 Hosting:     https://fastmcp.cloud                     │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

[12/19/25 21:28:34] INFO     Starting MCP server 'Demo 🚀' with   server.py:2527
                             transport 'stdio'                                  
```


## Question 3: Scrape Web Tool

Now let's create a tool for downloading content of any web page. 

We'll use Jina reader for that.

To get content of any page in markdown, you simply need to add `r.jina.ai` in front of the address. For example: `https://r.jina.ai/https://datatalks.club`

Ask your AI assistant to create a tool based on this. You can ask it to use the `requests` library. 

I also recommend testing it. I used a prompt like that:

```
Create a file `test.py` which invokes this function to test that it works well
```

Test it to retrieve the content of `https://github.com/alexeygrigorev/minsearch`. How many characters does it return? 


* 1184
* **9184** (answer)
* 19184
* 29184

Select the closest answer if you don't get the exact match.


## Question 4: Integrate the Tool

Integrate the MCP tool into your AI assistant. 

The command for running the MCP server is this:

```bash
uv --directory ~/path/to/homework run python main.py
```

(or `C:/Users/username/path/to/homework` if you're on Windows)

Replace the directory with the full path to this project

Ask it the following:

```
Count how many times the word "data" appears on https://datatalks.club/
Use available MCP tools for that
```

```
I'll call the repo's MCP fetch tool to retrieve the page markdown, then count occurrences of "data" (case-insensitive).

Ran fetch_markdown_tool my-mcp-server-7d3dec79 (MCP Server)
Counted word occurrences
Ran count_words_tool my-mcp-server-7d3dec79 (MCP Server)
I checked available MCP tools and used the repo's fetch/count tools.

MCP tools used: mcp_my-mcp-server_fetch_markdown_tool, mcp_my-mcp-server_count_words_tool.
Count of the word "data" (case-insensitive, whole-word) on https://datatalks.club/: 50.
```

What's the answer?

* **61** (closest answer)
* 111
* 161
* 261

Select the closest answer if you don't get the exact match.


## Question 5: Implement Search (2 points)

Now ask the agent to: 

* Download https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip. Don't download it if it's already downloaded
* Iterate over all zip files but read only md and mdx ones 
* Remove the first part of the path in the filename. So "fastmcp-main/docs/getting-started/welcome.mdx" becomes "docs/getting-started/welcome.mdx"
* Index these files with minsearch. Put the text content in "content" field and filename in "filename" 
* Use https://github.com/alexeygrigorev/minsearch to learn how to use minsearch
* Create a search function that retrieves 5 most relevant documents from the index
* Create search.py and test the implementation there


```You are an autonomous AI software agent. Your task is to implement a document indexing and search pipeline in Python.

GOAL:
Download documentation from a GitHub repository, index it using minsearch, and expose a search function.

TASKS (execute in order):

1. DOWNLOAD DATA
- Check if the file `fastmcp-main.zip` already exists locally.
- If it does NOT exist, download:
  https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip
- If it already exists, do NOT download again.

2. PROCESS ZIP FILES
- Iterate over ALL zip files found in the working directory.
- From each zip file:
  - Read ONLY files with extensions `.md` and `.mdx`
  - Ignore all other file types
- For each selected file:
  - Remove the first path component from the filename
    Example:
      "fastmcp-main/docs/getting-started/welcome.mdx"
      → "docs/getting-started/welcome.mdx"

3. INDEXING WITH MINSEARCH
- Use the `minsearch` library from:
  https://github.com/alexeygrigorev/minsearch
- Study the repository to understand:
  - How to create an index
  - How to add documents
  - How to perform a search
- Create an index where each document has:
  - "content": the full text of the markdown file
  - "filename": the cleaned filename (without the first path segment)

4. SEARCH FUNCTION
- Implement a function:
  
  search(query: str) -> List[dict]

- The function must:
  - Search the index
  - Return the 5 most relevant documents
  - Each result should include:
    - filename
    - relevance score (if available)
    - content snippet or full content

5. IMPLEMENTATION FILE
- Create a file named `search.py`
- `search.py` must:
  - Download the zip (if needed)
  - Build the index
  - Expose the search function
  - Include a simple test section (e.g. `if __name__ == "__main__":`)
    where several example queries are executed and printed

CONSTRAINTS:
- Use clean, readable Python code
- Use functions where appropriate
- Avoid unnecessary dependencies
- The code must be runnable locally with Python 3.10+

DELIVERABLES:
- A single file: `search.py`
- Fully working indexing and search logic
- Clear inline comments explaining important steps
```

```
== Query: demo
- examples/testing_demo/README.md (score=0.1856)
# FastMCP Testing Demo  A comprehensive example demonstrating FastMCP testing patterns with pytest-asyncio.  ## Overview  This example shows how to: - Set up pytest-asyncio configuration in `pyproject...
```

What's the first file returned that you get with the query "demo"? 

* README.md
* docs/servers/context.mdx
* **examples/testing_demo/README.md** (answer)
* docs/python-sdk/fastmcp-settings.mdx


## Question 6: Search Tool (ungraded)

Now you can ask your assistant to implement it as a tool in main.py - and voila, you have a documentation search engine in your AI assistant!


```
use MPC serach tool to search "demo" query and return the first file
```


```
Optimizing tool selection...

I'll run the MCP tsearch tool with query "demo" and return the top result.

Top result:

filename: examples/testing_demo/README.md
score: 0.18562546493819693
snippet: # FastMCP Testing Demo — A comprehensive example demonstrating FastMCP testing patterns with pytest-asyncio.
```


## Homework URL

Commit your code to GitHub. You can create a repository for this course. Within the repository, create a folder, e.g. "03-mcp", where you put the code.

Use the link to this folder in the homework submission form.

Respotitory url:

https://github.com/jelambrar96-datatalks/mcp-ai-demo


## Tip

You can copy-paste the homework description into the AI system of your choice. But make sure you understand (and follow) all the steps in the response.


## Submission

Submit your homework here: https://courses.datatalks.club/ai-dev-tools-2025/homework/hw3


## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Don't worry about being perfect. Everyone starts somewhere, and people love following genuine learning journeys!

### Example post for LinkedIn:

```
🚀 Week 3 of AI Dev Tools Zoomcamp by @DataTalksClub @Alexey Grigorev complete!

Just built my own MCP server - a documentation search engine!

Today I learned how to:

✅ Set up FastMCP and create custom tools
✅ Scrape web content with Jina Reader
✅ Index documentation with minsearch
✅ Integrate MCP tools with AI assistants
✅ Build a searchable knowledge base

Here's my repo: https://github.com/jelambrar96-datatalks/mcp-ai-demo

Following along with this amazing course - who else is exploring MCP?

You can sign up here: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/

#MCP #ModelContextProtocol
#AIEngineering #AIDevelopment
#zoomcamp #aidevtoolszoomcamp #datatalksclub
```

### Example post for Twitter/X:

```
🤖 Built an MCP server with AI in @Al_Grigor's course!

🔧 Custom MCP tools
🌐 Web scraping with Jina
🔍 Document search with minsearch
⚡ AI assistant integration

My repo: https://github.com/jelambrar96-datatalks/mcp-ai-demo

Join me: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/

#MCP #ModelContextProtocol
#AIEngineering #AIDevelopment
#zoomcamp #aidevtoolszoomcamp #datatalksclub
```
