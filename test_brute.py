import pytest
from brute import Brute
from pytest_mock import MockerFixture


todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        def it_returns_true_for_correct_guess(cracker):
            assert cracker.bruteOnce("TDD") is True 

        def it_returns_true_for_incorrect_guess(cracker):
            assert cracker.bruteOnce("wrong") is False

        def it_handles_empty_string_correctly(cracker):
            assert cracker.bruteOnce("") is False

        def it_is_case_sensitive(cracker):
            assert cracker.bruteOnce("tdd") is False

        def it_handles_large_strings_without_error(cracker):
            large_string = "A" * 1000
            assert cracker.bruteOnce(large_string) is False


    def describe_bruteMany():
        def it_returns_positive_time_on_succes(mocker: MockerFixture, cracker):
            mocker.patch.object(cracker, "randomGuess", return_value ="TDD")
            time_taken = cracker.bruteMany(limit = 10)
            assert time_taken > 0

        def it_returns_negative_one_on_failure(mocker: MockerFixture, cracker):
            mocker.patch.object(cracker, "randomGuess", return_value="wrong")
            result = cracker.bruteMany(limit=10)
            assert result == -1

        def it_stops_after_correct_guess(mocker: MockerFixture, cracker):
            mocker.patch.object(cracker, "randomGuess", side_effect=["wrong", "wrong", "TDD"])
            result = cracker.bruteMany(limit=5)
            assert result > 0

        def it_returns_negative_for_high_limit_without_success(mocker: MockerFixture, cracker):
         mocker.patch.object(cracker, "randomGuess", return_value="wrong")
         result = cracker.bruteMany(limit=100)
         assert result == -1


       

              

      