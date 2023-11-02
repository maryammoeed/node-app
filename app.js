const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  const filePath = path.join(__dirname, req.url);
  
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    const htmlContent = `
      <html>
        <head>
          <title>Hello, World!</title>
        </head>
        <body>
          <h1>Hello, World!</h1>
          <p>This is a simple Node.js web app.</p>
        </body>
      </html>
    `;
    res.end(htmlContent);
  } else {
    fs.access(filePath, fs.constants.R_OK, (err) => {
      if (!err) {
        const fileStream = fs.createReadStream(filePath);
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        fileStream.pipe(res);
      } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('File not found');
      }
    });
  }
});

const PORT = process.env.PORT || 8501;

server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
