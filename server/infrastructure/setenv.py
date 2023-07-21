import os


def src_dir():
    return os.path.abspath(os.path.join(module_dir(), '../src'))


def project_dir():
    return os.path.abspath(os.path.join(module_dir(), '../'))


def module_dir():
    return '/'.join(__file__.split('/')[:-1])


def env_file_path(*, template=False):
    return project_dir() + ('/.env.example' if template else '/.env')


if __name__ == '__main__':
    print('Getting env template')
    with open(env_file_path(template=True)) as env_template:
        content = env_template.read()
        content += '\n'
        content += 'PYTHONPATH=' + src_dir() + ':$PYTHONPATH' + '\n'

        print('Writing env file')
        with open(env_file_path(), 'w') as env_file:
            env_file.write(content)
