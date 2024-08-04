# codesplitter for generative AI

Many of the recent generative AIs, such as Chat-GPT, Copilot, etc., have a character limit when inputting. Since you can’t input long code all at once, you need to count the number of characters and split the code in advance before inputting it into the generative AI. This `codesplitter` allows you to easily split the code just by pressing a button, as long as you have a long code copied to the clipboard in advance.

## How to Use

1. Select all the code in the editor and copy it to the clipboard with `Ctrl+C` (or `Command+C` on Mac).
2. Launch `codesplitter` and press the “1. Press this button to paste your long code in Clipboard” button.
3. Select and press the button with the desired number of characters for splitting, located to the right of the section titled ‘2. Split Code into Segments’.
4. Buttons labeled “0”, “1”, “2”… will appear. Press “0” to put the first set of characters (based on the number you selected in step 3) into the clipboard, then paste (Ctrl+V, or Command+V on Mac) into the generative AI screen and press the execution button of the generative AI.
5. Once the generative AI’s response is complete, press “1”, then paste (`Ctrl+V`, or `Command+V` on Mac) into the generative AI screen and press the execution button of the generative AI.
6. Continue in the same way with “2” and so on. This will input all the code into the generative AI.

## Remark

Assuming instructions are being written for an AI, divide the text into segments that are 100 characters shorter than the selected character count.

## Creating the Executable File

By running pyinstaller codesplitter.spec in the terminal, a folder named codesplitter will be created inside the dist directory, and codesplitter.exe will be generated within it. Distributing this codesplitter folder will allow codesplitter to be executed on other computers. (Please do not delete the _internal folder as it is necessary.)
