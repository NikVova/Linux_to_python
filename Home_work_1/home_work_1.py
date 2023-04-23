import subprocess
import re
import string

"task_3_seminar"
# if __name__ == '__main__':
#     result = subprocess.run('cat /etc/os-release\n', shell=True,
#                             stdout=subprocess.PIPE, encoding='utf 8')
#     out = result.stdout
#     print(out)
#     # lines = '\n'.join(out)
#     lines = out.split('\n')
#     print(lines)
#
#     if result.returncode == 0:
#         if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lines and 'VERSION_CODENAME=jammy' in lines:
#             print('SUCCESS')
#         else:
#             print('FAIL')
#     else:
#         print('FAIL')


"task_1_home_work"
# if __name__ == '__main__':
#
#     def func(com: str, text: str):
#         result = subprocess.run(com, shell=True,
#                                 stdout=subprocess.PIPE, encoding='utf 8')
#         out = result.stdout
#         # print(out)
#         if result.returncode == 0:
#             if re.search(text, out):
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(False)
#
#
#     func('cat /etc/os-release', 'jammy')

"task_2_home_work_1"

# if __name__ == '__main__':
#
#     def func(com: str, text: str):
#         result = subprocess.run(com, shell=True,
#                                 stdout=subprocess.PIPE, encoding='utf 8')
#         out = result.stdout
#         for p in string.punctuation:
#             if p in out:
#                 out_rep = out.replace(p, ' ')
#
#         if result.returncode == 0:
#             if re.search(text, out_rep):
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(False)
#     func('cat /etc/os-release', '22.04.1')
