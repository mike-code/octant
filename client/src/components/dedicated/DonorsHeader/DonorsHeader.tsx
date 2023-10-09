import cx from 'classnames';
import React, { FC } from 'react';
import { useTranslation } from 'react-i18next';

import useProposalDonors from 'hooks/queries/useProposalDonors';

import styles from './DonorsHeader.module.scss';
import DonorsHeaderProps from './types';

const DonorsHeader: FC<DonorsHeaderProps> = ({
  proposalAddress,
  dataTest = 'DonorsHeader',
  className,
}) => {
  const { t } = useTranslation('translation', { keyPrefix: 'components.dedicated.donorsHeader' });

  const { data: proposalDonors, isFetching } = useProposalDonors(proposalAddress);

  return (
    <div className={cx(styles.header, className)} data-test={dataTest}>
      <span className={styles.headerLabel}>{t('donors')}</span>{' '}
      <div className={styles.count} data-test={`${dataTest}__count`}>
        {isFetching ? '--' : proposalDonors?.length}
      </div>
    </div>
  );
};

export default DonorsHeader;