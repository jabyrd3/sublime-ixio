sublime-ixio
============

Sublime Text 3 plugin to post to ix.io, as well as view any previous posts.

Usage: 

1. Edit ixio.sublime-settings with your ixio details. If you don't have ixio details just make something up. A new account will be created. Probably you shouldn't use a password that you use anywhere else as it's stored in plaintext in the config and ix.io uses basic HTTP auth.

2. Select the text you want post to ix.io if you want to paste selection. If you want to paste the entire file make sure the file you want to paste is the currently active buffer.

3. Press Shift+Ctrl+P (Shift+Cmd+P in OSX) to open the command pallete

4. Type 'ixio' and select ixio: post

5. Press enter.

6. The link to your paste will be copied to your clipboard.

7. If you'd like to see a list of your pastes open the command pallete and type 'ixio' then select ixio: pastes.

8. To open a paste from the list put the cursor on the first line of the paste and then right click.


Todo:

Add support for some of the more obscure ix.io features like self destructing pastes and deleting or editing pastes. Maybe syntax highlighting for pastes?
