## Pubquiz

This project is still work in progress and it's not intended to be published in production! I'm building it out of curiosity and fun.
The API is more or less done. Built with FastAPI and React.


## Installation

Install python requirements: `pip install -r requirements.txt`
Install react dependencies: `cd pubquiz/web && npm i` and bundle it with `npm run build`
Now you can start the application from the root directory with `python -m pubquiz`. It will mount the `pubquiz/web/build` folder as static assets and host it on `/`.

