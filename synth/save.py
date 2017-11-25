import subprocess

def execute_voice(data, dir_path, filename=None):
    if filename:
        # save sound to the file
        subprocess.Popen(["".join((dir_path, "/synth/tts/say.exe")), "-w",
                          "".join((dir_path, "/sounds/{}".format(filename))), data])
    else:
        # run sound
        subprocess.Popen(["".join((dir_path, "/synth/tts/say.exe")), data])