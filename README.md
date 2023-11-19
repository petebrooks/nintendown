# nintendown

## install

```bash
brew install ffmpeg scdl
poetry install
```

## run

```bash
poetry run python nintendown.py
```

## compile

```bash
poetry run pyinstaller --onefile --windowed nintendown.py
```

## gatekeeper

if necessary, you can temporarily disable gatekeeper on macos with the following command:

```bash
sudo spctl --master-disable
```

and re-enable it with:

```bash
sudo spctl --master-enable
```
