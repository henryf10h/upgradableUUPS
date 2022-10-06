// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "./uupsTokenV2.sol";

contract MyTokenV3 is MyToken {

    // we have to change state variables in the same order as in MyTokenV2,
    // only then we can append new state variables

    uint256 public fee;
    string public tax;

    function version() public pure returns (string memory){
        return "V3!";
    }
}