//==========================================================
//
// Finance Engine
//
//==========================================================

const chatWindow = document.getElementById("chatWindow");
const questionBox = document.getElementById("question");
const sendButton = document.getElementById("sendButton");
const uploadButton = document.getElementById("uploadButton");
const pdfFile = document.getElementById("pdfFile");

let pdfLoaded = false;


//==========================================================
//
// Chat Helpers
//
//==========================================================

function addUserMessage(message)
{
    addMessage(message, "user");
}

function addAssistantMessage(message)
{
    addMessage(message, "assistant");
}

function addMessage(message, type)
{
    const wrapper = document.createElement("div");

    wrapper.className = "message " + type;

    const bubble = document.createElement("div");

    bubble.className = "bubble";

    bubble.innerHTML = message;

    wrapper.appendChild(bubble);

    chatWindow.appendChild(wrapper);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}


//==========================================================
//
// Thinking
//
//==========================================================

function showThinking()
{
    const wrapper = document.createElement("div");

    wrapper.className = "message assistant";

    wrapper.id = "thinking";

    const bubble = document.createElement("div");

    bubble.className = "bubble";

    bubble.innerHTML = "🤖 Finance Engine is thinking...";

    wrapper.appendChild(bubble);

    chatWindow.appendChild(wrapper);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeThinking()
{
    const thinking = document.getElementById("thinking");

    if(thinking)
    {
        thinking.remove();
    }
}


//==========================================================
//
// Upload PDF
//
//==========================================================

uploadButton.onclick = async function()
{
    if(pdfFile.files.length === 0)
    {
        alert("Please select a PDF.");

        return;
    }

    const file = pdfFile.files[0];

    addAssistantMessage(
        "Uploading <b>" +
        file.name +
        "</b>..."
    );

    const formData = new FormData();

    formData.append("file", file);

    try
    {
        const response = await fetch("/upload",
        {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if(data.success)
        {
            pdfLoaded = true;

            addAssistantMessage(
                "✅ PDF Loaded Successfully.<br><br>" +
                "<b>" + data.filename + "</b>"
            );
        }
        else
        {
            addAssistantMessage(
                "❌ Upload Failed<br><br>" +
                data.error
            );
        }
    }
    catch(error)
    {
        addAssistantMessage(
            "❌ Backend not reachable."
        );

        console.error(error);
    }
};


//==========================================================
//
// Chat
//
//==========================================================

sendButton.onclick = async function()
{
    const question = questionBox.value.trim();

    if(question === "")
        return;

    if(!pdfLoaded)
    {
        alert("Please upload a PDF first.");

        return;
    }

    addUserMessage(question);

    questionBox.value = "";

    showThinking();

    try
    {
        const response = await fetch("/chat",
        {
            method: "POST",

            headers:
            {
                "Content-Type":"application/json"
            },

            body: JSON.stringify(
            {
                question: question
            })
        });

        const data = await response.json();

        removeThinking();

        if(data.success)
        {
            addAssistantMessage(data.answer);
        }
        else
        {
            addAssistantMessage(
                "❌ " + data.error
            );
        }
    }
    catch(error)
    {
        removeThinking();

        addAssistantMessage(
            "❌ Unable to contact backend."
        );

        console.error(error);
    }
};


//==========================================================
//
// ENTER
//
//==========================================================

questionBox.addEventListener("keydown", function(event)
{
    if(event.key === "Enter")
    {
        sendButton.click();
    }
});


//==========================================================
//
// Backend Health Check
//
//==========================================================

async function checkHealth()
{
    try
    {
        const response = await fetch("/health");

        const data = await response.json();

        console.log(data);

        addAssistantMessage(
            "🟢 Finance Engine Ready"
        );
    }
    catch(error)
    {
        addAssistantMessage(
            "🔴 Backend Offline"
        );
    }
}

checkHealth();
