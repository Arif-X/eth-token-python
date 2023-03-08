pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract JancokToken is ERC20 {
    constructor() public ERC20("Jancok Token", "JT") {
        _mint(msg.sender, 100000000);
    }
}
