const http = require('http');
const fs = require('fs');
const path = require('path');
const mime = require('mime');

const server = http.createServer((req, res) => {
  const filePath = path.join(__dirname, req.url);

  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    const jsonResponse = {
      message: "Welcome to the Node.js server!",
      description: "This server handles different content types and responses.",
      success: true
    };
    res.end(JSON.stringify(jsonResponse));
  } else if (req.url === '/image') {
    const imagePath = path.join(__dirname, 'image.jpg'); // Example image path
    fs.access(imagePath, fs.constants.R_OK, (err) => {
      if (!err) {
        const fileStream = fs.createReadStream(imagePath);
        res.statusCode = 200;
        res.setHeader('Content-Type', mime.getType(imagePath));
        fileStream.pipe(res);
      } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Image not found');
      }
    });
  } else {
    fs.access(filePath, fs.constants.R_OK, (err) => {
      if (!err) {
        const extname = path.extname(filePath);
        res.statusCode = 200;
        res.setHeader('Content-Type', mime.getType(extname) || 'application/octet-stream');
        const fileStream = fs.createReadStream(filePath);
        fileStream.pipe(res);
      } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('File not found');
      }
    });
  }
});

const PORT = 8081;  
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
