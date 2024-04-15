<p align="center">
 <img width=300px height=300px src="https://imgur.com/042gx4E.png" alt="Project logo">
</p>

<h1 align="center">GenDiff</h1>

<div align="center">

### Hexlet tests, CI tests, maintainability, test coverage status:
[![Actions Status](https://github.com/Pythonusus/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Pythonusus/python-project-50/actions)
[![Actions Status](https://github.com/Pythonusus/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Pythonusus/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2a82e8b1b0f8354ce79e/maintainability)](https://codeclimate.com/github/Pythonusus/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2a82e8b1b0f8354ce79e/test_coverage)](https://codeclimate.com/github/Pythonusus/python-project-50/test_coverage)

</div>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Logo](#logo)


## 🧐 About <a name = "about"></a>

GenDiff is a command-line utility that compares two JSON or YAML files and generates a difference.

GenDiff supports different formats of output such as TXT, JSON or YAML.

You can also use GenDiff as a library or dependency to your project.

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

1. Python >= 3.12
2. pip >= 23.3.1
3. Poetry >= 1.7.1

### Installing

1. Clone GitHub repo: 
```
git clone https://github.com/Pythonusus/python-project-50
```
2. Create virtual environment and install dependencies. This comman should be executed in the root directory of the project:
```
make install
```

3. Build project:
```
make build
```

4. Install project on user level (`home/<user-name>/.local/bin` for Linux users):
```
make package-install
```

5. If you receive a warning on step 4:
`WARNING: The script gendiff is installed in 'path/to/your/executable' which is not on PATH.`
add this directory to `PATH` for current shell session:
```
export PATH=$PATH:'path/to/your/executable'
```

To set it permanently for all future bash sessions add `export PATH=$PATH:'path/to/your/executable'` to your `.bashrc` file in your `$HOME` directory.

6. GenDiff is ready to use!

### Installation example:
[![asciicast](https://asciinema.org/a/SWYYefdsYygkavDCyW1gInlrk.svg)](https://asciinema.org/a/SWYYefdsYygkavDCyW1gInlrk)

## 🎈 Usage <a name="usage"></a>

### `gendiff` command will become available in the command line after installation

To compare two JSON or YAML files use:
```
gendiff path/to/file1 path/to/file2
```

### You can set format of the output using `-f` or `--format` flag

Available formats:
- stylish (default)
- plain
- json
- yaml

```
gendiff path/to/file1 path/to/file2 -f plain
```
### Stylish format example for plain structures:
[![asciicast](https://asciinema.org/a/xvpRopjyBAT2eFKnpG1UX7NSG.svg)](https://asciinema.org/a/xvpRopjyBAT2eFKnpG1UX7NSG)

### Stylish format example for nested structures:
[![asciicast](https://asciinema.org/a/m9SEtrCyd1U4J7tLDRqSd7o8T.svg)](https://asciinema.org/a/m9SEtrCyd1U4J7tLDRqSd7o8T)

### Plain format example:
[![asciicast](https://asciinema.org/a/9opCs6LTeKj0X0c0nuyj9ATWk.svg)](https://asciinema.org/a/9opCs6LTeKj0X0c0nuyj9ATWk)

### Json format example:
[![asciicast](https://asciinema.org/a/h8w8WOUxe4YfS9ridGpoyXY8G.svg)](https://asciinema.org/a/h8w8WOUxe4YfS9ridGpoyXY8G)

### Yaml format example:
[![asciicast](https://asciinema.org/a/JmHscntBBwy49HTYRZQG8zZe3.svg)](https://asciinema.org/a/JmHscntBBwy49HTYRZQG8zZe3)

### To see help use `-h` or `--help` flag
```
gendiff -h
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Poetry](https://python-poetry.org) - Python packaging and dependency management tool
- [PyYAML](https://pyyaml.org) - A full-featured YAML framework for the Python programming language

## ✍️ Authors <a name = "authors"></a>

[@Pythonusus](https://github.com/kylelobo)

## Logo <a name = "logo"></a>
Made with [Ideogram AI](https://ideogram.ai/)

Stored at [imgur.com](https://imgur.com/)