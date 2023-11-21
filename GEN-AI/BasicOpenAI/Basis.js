const fs = require('fs');
const express = require('express');
const app = express();
app.use(express.static(__dirname + '/public')); //__dir and not _dir
const port = 8000; // you can use any port
app.listen(port);
console.log('server on ' + port);

try {  
    var API_KEY = fs.readFileSync('OPEN_AI_KEY.txt', 'utf8');
    console.log(API_KEY.toString());    
} catch(e) {
    console.log('Error:', e.stack);
}

url = 'https://api.openai.com/v1/chat/completions'



async function chat_openai(){
    const response = await fetch(url,{
        method :'POST',
        headers: {
            Authorization: `Bearer ${API_KEY}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "model": 'gpt-3.5-turbo',
            "messages": [{"role": "user", "content": "Say this is a test!"}], 
            "temperature": 0.7
            })
        })
        const data = await response.json()
        console.log(data)
}
chat_openai()
async function fetch_data_openai(){
    const response = await fetch(url,{
    method :'POST',
    headers: {
        Authorization: `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        model: 'text-davinci-003',
        prompt: 'hello how are you today?',
        max_tokens: 7
        })
    })
    const data = await response.json()
    console.log(data)
}
//fetch_data_openai()

/**
 * model            top_p           presence_penalty
 * prompt           n               frequency_penalty
 * suffix           streams         best_of
 * max_token        log_probs       logit_bias
 * temperature      echo            user
*/

/**
 * Rules of Prompt Creation
 * 1. Show and Tell: Lead by providing and example of what you want to create
 * 2. Provide Quality Data: Be sure to proof read your examples
 * 3. Check Your Settings: Your temperature and top_p settings control how deterministic the model is in generating a response
 */