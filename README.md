socsec 
-----------

**sosec** is a command-line toolkit for automated credential testing and HTTP request orchestration on social media platforms. It enables structured interaction with platform endpoints through configurable workflows and input datasets. sosec supports Linux and Windows environments. 

![](https://img.shields.io/github/stars/samueleamato/sosec)
![](https://img.shields.io/github/forks/samueleamato/sosec)
![](https://img.shields.io/github/issues/samueleamato/sosec)

> [!WARNING]
> This project is intended for educational and authorized testing purposes only. 
> Do not perform actions on accounts or services without explicit permission.

### Documentation quick links

* [Installation](#installation)
* [Quick Start](#quick-start)
* [Contributing](#contributing)
* [Community](#community)

Licensed under MIT License.

### installation

If you are on **Linux**, you can install sosec with the following command:

```
git clone https://github.com/samueleamato/sosec && cd sosec && bash install.sh
```

If you are on **Windows**, you can install sosec with the following command:

```
powershell -Command "Invoke-WebRequest -Uri https://github.com/samueleamato/sosec/archive/refs/heads/main.zip -OutFile main.zip; Expand-Archive main.zip -DestinationPath .; cd .\sosec-main\cmd; pip install -r requirements.txt; cd ..; start windows.bat"
```

### Quick start

Run the TUI interface:

```
python3 sosec.py
```

The interface will guide you through module selection and configuration directly from the terminal.

**Basic Workflow**

1) Launch the TUI.
2) Choose the target platform.
3) Provide required inputs when prompted.
4) Review output directly in the terminal.

### Contributing

Contributions are welcome. Please open an issue to discuss major changes before submitting a pull request.

### Community

Join the official Discord server to discuss issues, get help, or contribute:

[Discord!](https://discord.com/invite/3r6mkjv6AP)

