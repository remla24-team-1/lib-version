import subprocess

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            git_version = subprocess.check_output(['git', 'describe', '--tags']).strip().decode('utf-8')
            return git_version
        except Exception as e:
            print(f"Error retrieving version from Git tags: {e}")
            return "Unknown"

if __name__ == "__main__":
    print(f"Library Version: {VersionUtil.get_version()}")
