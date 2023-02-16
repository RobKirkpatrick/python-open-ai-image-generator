# python-open-ai-image-generator
A quick python script for getting up and running with Open AI's Image Generator

# **Using Open AI’s image generator**

This  tutorial explains how to use Open AI's image generator to create stunning images using Visual Studio Code (VSCode) and Python. I'll walk you through the process, including how to set up a Python environment, install OpenAI, generate an API key, and use the image generation script. With a few simple steps, you can be up and running in no time, creating and manipulating images with the power of Open AI's image generator and Python. Have fun and get creative!

### **Start here if you do not have a Python environment set-up already**

For this tutorial, I’ll walk you through the process I completed on my MacBook with VSCode. There are dozens of other Python environments that you can use for this, and of course you can use your Windows machine (as much as my inner Apple fan-boy doesn’t want you to).

- VSCode installation. [https://code.visualstudio.com/](https://code.visualstudio.com/)
- PATH set-up. [https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line)
- Open a new terminal window in VSCode
- Install Homebrew. [https://brew.sh/](https://brew.sh/)
    
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    
    - Once that finishes, don’t neglect the 2 steps displayed in the terminal. You’ll need to run two commands which can be copied and pasted, and then run by hitting “return”
        - Everything that is displayed on the first line that looks like the code below (you’ll see you home directory after the “>>” make sure that you copy that too
        
        ```
        (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >>
        ```
        
        - Everything on the second line
        
        ```
            eval "$(/opt/homebrew/bin/brew shellenv)"
        ```
        
- Installing Python. [https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
    - I do like to complete the “Hello World” Tutorial on a fresh build, but you by no means need to do so
- Upgrade pip
    
    ```
    python3.11 -m pip install --upgrade pip
    ```
    

### **Getting Started with OpenAI**

- [Register for an account](https://openai.com/api/) if you don’t currently have one
- Return to VSCode and Install “OpenAI”
    - Note: If you’ve set-up your environment differently than the steps I outlined above, this input may be different for you
    
    ```
    python3 -m pip install openai
    ```
    
- [Copy the example code from Open Ai](https://platform.openai.com/docs/api-reference/authentication) (make sure you use the Python script)
    
    ```
    import os
    import openai
    openai.organization = "org-Rw9He2WlfsUmXrXLU27JLuPK"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    ```
    
    - 3 edits I made to this code
        - Comment out ‘openai.organization’ as I don’t have an Org ID currently
            - If you do sign up for a team Open AI account, you should update this ‘org_id’
        - Comment out ‘openai.Model.list()’ as this is not required for this image generation
        - The method that this code is using above is attempting to store your API key in a variable. This is more secure, however since I am the only one using this file, I hardcoded the API key
            - **USE CAUTION WITH THIS METHOD IF SHARING THIS SCRIPT WITH OTHERS**
    - The resulting code with edits looks like the following
        
        ```
        import os
        import openai
        #openai.organization = "YOUR_ORG_ID"
        openai.api_key = 'YOUR_API_KEY'
        #openai.Model.list()
        ```
        
- [Generate an API Key](https://platform.openai.com/account/api-keys) on your OpenAI account
- Paste in between the ‘ ’ on the above code
- Retrieve the [image generation script from OpenAI](https://platform.openai.com/docs/guides/images/introduction)
    
    ```
    response = openai.Image.create(
      prompt="a white siamese cat",
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    ```
    
    - I made 1 edit for ease to display the link
        
        ```
        print(response)
        ```
        
- All together you code should look like the follow (don’t forget to update your API key)
    
    ```
    import os
    import openai
    #openai.organization = "YOUR_ORG_ID"
    openai.api_key = 'YOUR_API_KEY'
    #openai.Model.list()
    
    response = openai.Image.create(
      prompt="a white siamese cat",
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    
    print(response)
    ```
    
    - ‘n’ is a reference to the number of images you would like to generate. This is will accept a value from 1-10
    - ‘size’ corresponds to the image dimensions you would like. You can choose between
        - 256x256
        - 512x512
        - 1024x1024
- Now that you have your code compiled, all that’s left is the play with the ‘prompt’ by adding your idea in between the “ “ on line 8

### **Things to Note**

- The images that you generate are only accessible via the URL for 1 hour, so if you love something, make sure that you download it
- You have a limited number of calls that you are allotted on your OpenAI account. You can [track how many you’ve made here](https://platform.openai.com/account/usage)
- Another fun use of AI; you can have this code explained to you by pasting it into OpenAI’s chat bot, or [Denigma](https://denigma.app/#demo) (I’ll give them a shout-out since they were first I used for AI code description)
- Don’t forget that you can use [OpenAI](https://chat.openai.com/) to make this code better. One obvious improvement would be to have the URL shortened and made easier to open in a web browser

### **My favorite result so far**

```
prompt = "a baby panda"
```

You can see this image on [my website](http://robkirkpatrick.com/ai-image-generator/)
