# Set PATH, MANPATH, etc., for Homebrew
#set -gx HOMEBREW_PREFIX "/opt/homebrew";
#set -gx HOMEBREW_CELLAR "/opt/homebrew/Cellar";
#set -gx HOMEBREW_REPOSITORY "/opt/homebrew";
#set -q PATH; or set PATH ''; set -gx PATH "/opt/homebrew/bin" 
#"/opt/homebrew/sbin" $PATH;
#set -q MANPATH; or set MANPATH ''; set -gx MANPATH "/opt/homebrew/share/man" 
#$MANPATH;
#set -q INFOPATH; or set INFOPATH ''; set -gx INFOPATH 
#"/opt/homebrew/share/info" $INFOPATH;

###################################
# Interactive mode configurations #
###################################
set -gx NNN_FIFO /tmp/nnn.fifo
set -gx NNN_SSHFS_OPTS sshfs -o follow_symlinks
set -gx NNN_USE_EDITOR 1
set -gx NNN_COLORS 2136
set -gx NNN_OPENER xdg-open
set -gx NNN_TRASH 2 # configure gio trash
set -gx NNN_FCOLORS 030304020000060801030500 # filetype colors. this mimics dircolors
# d: detail mode
# e: open text files in terminal
# u: use selection, don't prompt to choose between selection and hovered entry
# r: show cp/mv progress
# U: show file's owner and group in status bar

set -gx NNN_PLUG 'o:fzopen;p:mocq;d:diffs;t:nmount;v:imgview;f:preview-tui'
