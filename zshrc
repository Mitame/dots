#
# User configuration sourced by interactive shells
#

# Source zim
if [[ -s ${ZDOTDIR:-${HOME}}/.zim/init.zsh ]]; then
  source ${ZDOTDIR:-${HOME}}/.zim/init.zsh
fi
# Created by newuser for 5.2 #

# Overwrite files when using `x > y`
setopt clobber

# SSH servers don't like termite
[[ "$TERM" == "xterm-termite" ]] && \
  alias ssh="TERM=xterm ssh"


# Prompt stuffs
autoload -Uz promptinit
promptinit
prompt eriner


# Fix killall not listing all proccesses on tab
zstyle ':completion:*:processes' command 'NOCOLORS=1 ps -U $(whoami)|sed "/ps/d"'
zstyle ':completion:*:processes' insert-ids menu yes select
zstyle ':completion:*:processes-names' command 'NOCOLORS=1 ps xho command|sed "s/://g"'
zstyle ':completion:*:processes' sort false

# The following lines were added by compinstall
zstyle ':completion:*' completer _complete _ignored _correct _approximate
zstyle ':completion:*' matcher-list '' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|[._-]=** r:|=**' 'l:|=* r:|=*'
zstyle :compinstall filename '/home/emati/.zshrc'
autoload -Uz compinit
compinit
# End of lines added by compinstall
