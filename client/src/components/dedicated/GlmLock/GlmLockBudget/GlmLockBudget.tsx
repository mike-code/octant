import { useFormikContext } from 'formik';
import { AnimatePresence, motion } from 'framer-motion';
import React, { FC } from 'react';

import BudgetBox from 'components/dedicated/BudgetBox/BudgetBox';
import { FormFields } from 'components/dedicated/GlmLock/types';

import styles from './GlmLockBudget.module.scss';
import GlmLockBudgetProps from './types';

const variants = {
  hide: {
    height: '0',
    margin: '0',
    opacity: '0',
    zIndex: '-1',
  },
  show: {
    height: '0',
    margin: '0',
    opacity: '0',
    zIndex: '-1',
  },
  visible: {
    height: 'auto',
    margin: '0 auto 1.6rem',
    opacity: 1,
    zIndex: '1',
  },
};

const GlmLockBudget: FC<GlmLockBudgetProps> = ({ isVisible }) => {
  const { errors } = useFormikContext<FormFields>();

  return (
    <AnimatePresence initial={false}>
      {isVisible && (
        <motion.div
          animate="visible"
          className={styles.wrapper}
          exit="hide"
          initial="show"
          transition={{ ease: 'linear' }}
          variants={variants}
        >
          <BudgetBox
            isCurrentlyLockedError={errors.valueToDeposeOrWithdraw === 'cantUnlock'}
            isWalletBalanceError={errors.valueToDeposeOrWithdraw === 'dontHaveEnough'}
          />
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default GlmLockBudget;
