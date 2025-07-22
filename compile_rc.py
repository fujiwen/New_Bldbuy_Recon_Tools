import os
import subprocess

def compile_resource():
    # 资源文件路径
    rc_file = 'app.rc'
    res_file = 'app.res'
    
    # 检查 .rc 文件是否存在
    if not os.path.exists(rc_file):
        # 创建 .rc 文件
        rc_content = '''
#include <windows.h>

IDI_ICON1 ICON "app.ico"
'''
        with open(rc_file, 'w', encoding='utf-8') as f:
            f.write(rc_content)
    
    # 使用 windres 编译资源文件
    try:
        subprocess.run(['windres', rc_file, '-O', 'coff', '-o', res_file], check=True)
        print(f'成功编译资源文件: {res_file}')
    except subprocess.CalledProcessError as e:
        print(f'编译资源文件时出错: {e}')
        return False
    except FileNotFoundError:
        print('错误: 未找到 windres 命令，请确保已安装 MinGW-w64')
        return False
    
    return True

if __name__ == '__main__':
    compile_resource()