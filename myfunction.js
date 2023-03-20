
const inputs = document.querySelectorAll('input');
const codeBlock = document.getElementById('code-block');
const code = document.getElementById('code');
const form = document.querySelector('form');

const button = document.querySelector('button[type="button"]');

button.addEventListener('click', function() {
    // Get the code entered in the inputs
    const userCode = [...inputs].map((input) => input.value).join('');
  
    // Construct the path to the Internet shortcut file
    const filePath = `I:\\MECH\\SHA\\Motion Analyzer\\${userCode}.url`;

    // Check if the file exists
    fs.stat(filePath, function(err, stat) {
      if (err) {
        // Show an error message if the file is not found or if an error occurs
        alert('File not found');
      } else {
        // Open the Internet shortcut file
        window.open(filePath);
      }
    });
});
