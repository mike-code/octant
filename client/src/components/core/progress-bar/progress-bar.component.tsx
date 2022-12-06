import React, { FC } from 'react';
import cx from 'classnames';

import { tick } from 'svg/misc';
import Svg from 'components/core/svg/svg.component';

import ProgressBarProps from './types';
import styles from './styles.module.scss';

const ProgressBar: FC<ProgressBarProps> = ({ currentStepIndex, steps }) => (
  <div className={styles.progressBar}>
    {steps.map((step, index) => {
      const isDone = index < currentStepIndex;
      const isCurrent = index === currentStepIndex;
      return (
        // eslint-disable-next-line react/no-array-index-key
        <div key={index} className={cx(styles.element, isCurrent && styles.isCurrent)}>
          <div className={cx(styles.dot, isDone && styles.isDone, isCurrent && styles.isCurrent)}>
            {isDone && <Svg classNameSvg={styles.tick} img={tick} size={0.8} />}
          </div>
          {step}
        </div>
      );
    })}
  </div>
);

export default ProgressBar;
