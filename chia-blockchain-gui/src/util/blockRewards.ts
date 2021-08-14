import Big from 'big.js';

const MOJO_PER_CHIA = Big(1000000000000);
const BLOCKS_PER_YEAR = 1681920;
const BLOCKS_PER_MONTH = 138240;

export function calculatePoolReward(height: number): Big {
  if (height === 0) {
    return MOJO_PER_CHIA.times(1).times(1 / 3);
  }

  if (height ===1 ) {
    return MOJO_PER_CHIA.times(66666).times(1 / 3);
  }

  if (height < 1 * BLOCKS_PER_MONTH) {
    return MOJO_PER_CHIA.times(18).times(1 / 3);
  }
  if (height < 3 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(6).times(1 / 3);
  }
  if (height < 6 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(3).times(1 / 3);
  }
  if (height < 9 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(1.5).times(1 / 3);
  }
  if (height < 12 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(0.75).times(1 / 3);
  }

  return MOJO_PER_CHIA.times(0.375).times(1 / 3);
}

export function calculateBaseFarmerReward(height: number): Big {
  if (height === 0) {
    return MOJO_PER_CHIA.times(1).times(2 / 3);
  }
  if (height ===1 ) {
    return MOJO_PER_CHIA.times(66666).times(2 / 3);
  }
  if (height < 1 * BLOCKS_PER_MONTH) {
    return MOJO_PER_CHIA.times(18).times(2 / 3);
  }
  if (height < 3 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(6).times(2 / 3);
  }
  if (height < 6 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(3).times(2 / 3);
  }
  if (height < 9 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(1.5).times(2 / 3);
  }
  if (height < 12 * BLOCKS_PER_YEAR) {
    return MOJO_PER_CHIA.times(0.75).times(2 / 3);
  }

  return MOJO_PER_CHIA.times(0.375).times(2 / 3);
}
