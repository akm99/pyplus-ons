from pathlib import Path
import pytest
import subprocess

TEST_CASES_STDIN = [
    ("../day1/strings/solutions/exercise1.py", "Han Solo"),
    ("../day1/strings/solutions/exercise2.py", "172.16.21.10"),
    ("../day1/numbers/solutions/exercise1.py", "20\n8"),
    ("../day1/lists/solutions/exercise2.py", "172.16.21.10"),
]

TEST_CASES = [
    "../day1/files/solutions/exercise1.py",
    "../day1/lists/solutions/exercise1.py",
    "../day1/dictionaries/solutions/exercise1.py",
    "../day1/loops/solutions/exercise3.py",
    "../day1/loops/solutions/exercise1.py",
    "../day1/loops/solutions/exercise2.py",
    "../day1/exceptions/solutions/exercise1.py",
    "../day1/recap/solutions/exercise1.py",
    "../day1/recap/solutions/exercise2.py",
]


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def subprocess_runner_stdin(cmd_list, stdin_response, exercise_dir):
    with subprocess.Popen(
        cmd_list,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # Use line-buffering (send line when a newline is encountered)
        universal_newlines=True,  # Input/output gets converted to/from text
        cwd=exercise_dir,
    ) as proc:
        std_out, std_err = proc.communicate(input=stdin_response)
    return (std_out, std_err, proc.returncode)


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner(test_case):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""


@pytest.mark.parametrize("test_case,stdin_response", TEST_CASES_STDIN)
def test_runner_stdin(test_case, stdin_response):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner_stdin(cmd_list, stdin_response, script_dir)
    assert return_code == 0
    assert std_err == ""
