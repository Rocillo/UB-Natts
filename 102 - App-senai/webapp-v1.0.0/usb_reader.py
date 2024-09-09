import subprocess

# Substitua <instance_id> pelo InstanceID do dispositivo
instance_id = "HID\VID_FFFF&PID_0035&REV_0100&MI_00"  # Exemplo
subprocess.run(f'powershell Disable-PnpDevice -InstanceId "{instance_id}" -Confirm:$false', shell=True)
