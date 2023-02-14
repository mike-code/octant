const SPACER = '_';
const getLocalStorageKey = (prefix: string, suffix: string): string =>
  `${prefix}${SPACER}${suffix}`;

const allocationPrefix = 'allocation';
export const ALLOCATION_ITEMS_KEY = getLocalStorageKey(allocationPrefix, 'items');

const onboardingPrefix = 'onboarding';
export const IS_ONBOARDING_DONE = getLocalStorageKey(onboardingPrefix, 'isOnboardingDone');

const settingsPrefix = 'settings';
export const IS_ONBOARDING_ALWAYS_VISIBLE = getLocalStorageKey(
  settingsPrefix,
  'isOnboardingAlwaysVisible',
);
