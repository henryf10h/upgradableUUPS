// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "./uupsToken.sol";

contract MyTokenV2 is MyToken {

    uint256 public fee;

    function version() public pure returns (string memory){
        return "V2!";
    }
}