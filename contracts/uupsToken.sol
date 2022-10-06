// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelinupgradable/contracts/token/ERC20/ERC20Upgradeable.sol";
import "@openzeppelinupgradable/contracts/access/OwnableUpgradeable.sol";
import "@openzeppelinupgradable/contracts/proxy/utils/Initializable.sol";
import "@openzeppelinupgradable/contracts/proxy/utils/UUPSUpgradeable.sol";

contract MyToken is Initializable, ERC20Upgradeable, OwnableUpgradeable, UUPSUpgradeable {
    /// @custom:oz-upgrades-unsafe-allow constructor
    // constructor() {
    //     _disableInitializers();
    // }

    function initialize() initializer public {
        __ERC20_init("MyToken", "MTK");
        __Ownable_init();
        __UUPSUpgradeable_init();

        _mint(msg.sender, 67 * 10 ** decimals());
    }

    function _authorizeUpgrade(address newImplementation)
        internal
        onlyOwner
        override
    {}
}
