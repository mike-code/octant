import React from 'react';
import { Trans } from 'react-i18next';

import Button from 'components/core/Button/Button';
import styles from 'components/dedicated/ModalOnboarding/ModalOnboarding.module.scss';
import { Step } from 'components/dedicated/ModalOnboarding/types';
import { DISCORD_LINK, OCTANT_DOCS, BLOG_POST } from 'constants/urls';
import i18n from 'i18n';

const steps: Step[] = [
  {
    header: i18n.t('views.onboarding.steps.welcomeToOctant.header'),
    image: 'images/onboarding/1.webp',
    imageClassName: styles.welcomeToOctant,
    text: (
      <Trans
        components={[<Button href={BLOG_POST} variant="link3" />]}
        i18nKey="views.onboarding.steps.welcomeToOctant.text"
      />
    ),
  },
  {
    header: i18n.t('views.onboarding.steps.stakingRewards.header'),
    image: 'images/cycle.webp',
    imageClassName: styles.earnRewards,
    text: (
      <Trans
        components={[<span className={styles.bold} />]}
        i18nKey="views.onboarding.steps.stakingRewards.text"
      />
    ),
  },
  {
    header: i18n.t('views.onboarding.steps.allocateOrWithdraw.header'),
    image: 'images/favourites.webp',
    imageClassName: styles.allocateOrWithdraw,
    text: (
      <Trans
        components={[<span className={styles.bold} />]}
        i18nKey="views.onboarding.steps.allocateOrWithdraw.text"
      />
    ),
  },
  {
    header: i18n.t('views.onboarding.steps.moreInformation.header'),
    image: 'images/rewards.webp',
    imageClassName: styles.moreInformation,
    text: (
      <Trans
        components={[
          <span className={styles.bold} />,
          <Button href={OCTANT_DOCS} variant="link3" />,
          <Button href={DISCORD_LINK} variant="link3" />,
        ]}
        i18nKey="views.onboarding.steps.moreInformation.text"
      />
    ),
  },
];

export default steps;
