# Waybar ISS Urine Tank Module

Inspired by [pISSStream](https://github.com/Jaennaet/pISSStream/)

[Waybar](https://github.com/Alexays/Waybar) Module to show the current ISS urine tank capacity.

---

## Requirements
  
- A nerd font in your waybar stylesheet, if you plan to use the same icon format  
- `lightstreamer-client-lib` for Python
- Internet connection

---

## Installation

### Add the following to your `config.jsonc` in Waybar:

```jsonc
"custom/pISS": {
    "exec": "path/to/your/venv/bin/python path/to/your/piss_monitor.py",
    "return-type": "json",
    "interval": 0,
    "format": "{text} {icon}",
    "tooltip-format": "ISS Urine Tank: {text}",
    "format-icons": ["󰂎", "󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"]
}
```

---

### Script:

In the path where you want to install the script:

```bash
git clone https://github.com/krypt0graphy/waybar-pISS.git
./install.sh
```

Copy the `exec` line given in the Waybar module.

---

### Manual:

```bash
git clone https://github.com/krypt0graphy/waybar-pISS.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add the `exec` line in the Waybar module.


Style with custom-pISS in your stylesheet :)

![Screenshot, wallpaper by @ceramicnoise](https://github.com/krypt0graphy/waybar-pISS/blob/main/screenshot.png?raw=true)