# codesplitter

Many of the recent generative AIs, such as Chat-GPT, Copilot, etc., have a character limit when inputting. Since you can’t input long code all at once, you need to count the number of characters and split the code in advance before inputting it into the generative AI. This `codesplitter` allows you to easily split the code just by pressing a button, as long as you have a long code copied to the clipboard in advance.

## How to Use

1. Select all the code in the editor and copy it to the clipboard with `Ctrl+C` (or `Command+C` on Mac).
2. Launch `codesplitter` and press the “Press this button to paste your long code in Clipboard” button.
3. Press the “Split Code into Segments of 8000 Characters” button.
4. Buttons labeled “0”, “1”, “2”… will appear. Press “0” to put the first 8000 characters into the clipboard, then paste (`Ctrl+V`, or `Command+V` on Mac) into the generative AI screen and press the execution button of the generative AI.
5. Once the generative AI’s response is complete, press “1”, then paste (`Ctrl+V`, or `Command+V` on Mac) into the generative AI screen and press the execution button of the generative AI.
6. Continue in the same way with “2” and so on. This will input all the code into the generative AI.
