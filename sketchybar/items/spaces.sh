#!/usr/bin/env sh


SPACE_ICONS=("dev" "term" "web" "note" "misc" "social" "web" "media" "9" "10")

for i in "${!SPACE_ICONS[@]}"
do
  sid=$(($i+1))
  sketchybar --add space space.$sid left                                 \
             --set space.$sid associated_space=$sid                      \
                              icon=${SPACE_ICONS[i]}                     \
                              icon.padding_left=8                        \
                              icon.padding_right=8                       \
                              icon.highlight_color=$RED                  \
                              background.padding_left=5                  \
                              background.padding_right=5                 \
                              background.color=0x44ffffff                \
                              background.corner_radius=5                 \
                              background.height=22                       \
                              background.drawing=off                     \
                              label.drawing=off                          \
                              click_script="yabai -m space --focus $sid"
done

sketchybar   --add item       separator left                          \
             --set separator  icon=                                  \
                              icon.font="Hack Nerd Font:Regular:16.0" \
                              background.padding_left=20              \
                              background.padding_right=15             \
                              label.drawing=off                       \
                              associated_display=active               \
                              icon.color=$WHITE
