import cx from 'classnames';
import { AnimatePresence, motion } from 'framer-motion';
import React from 'react';

import Button from 'components/core/Button/Button';
import Img from 'components/core/Img/Img';
import Svg from 'components/core/Svg/Svg';
import useMediaQuery from 'hooks/helpers/useMediaQuery';
import { cross, info } from 'svg/misc';

import styles from './TipTile.module.scss';
import { TipTileProps } from './types';

const TipTile: React.FC<TipTileProps> = ({
  className,
  dataTest = 'TipTile',
  image,
  infoLabel,
  isOpen,
  onClose,
  text,
  title,
}) => {
  const { isDesktop } = useMediaQuery();

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          animate={{
            height: isDesktop ? ['0', '19.2rem', '19.2rem'] : ['0', '20rem', '20rem'],
            marginBottom: isDesktop ? ['0', '2.8rem', '2.8rem'] : ['0', '1.6rem', '1.6rem'],
            opacity: [0, 0, 1],
          }}
          className={cx(styles.root, className)}
          data-test={dataTest}
          exit={{
            height: isDesktop ? ['19.2rem', '19.2rem', '0'] : ['20rem', '20rem', '0'],
            marginBottom: isDesktop ? ['2.8rem', '2.8rem', '0'] : ['1.6rem', '1.6rem', '0'],
            opacity: [1, 0.1, 0],
          }}
          transition={{
            delay: 0.01,
            duration: 0.3,
            // easeOutCubic
            ease: x => 1 - (1 - x) ** 3,
            mass: 1.5,
            stiffness: 800,
          }}
        >
          <div>
            <div className={styles.info}>
              <Svg img={info} size={3.2} />
              <div className={styles.infoLabel}>{infoLabel}</div>
            </div>
            <div className={styles.body}>
              <div className={styles.title}>{title}</div>
              <div className={styles.text}>{text}</div>
            </div>
          </div>
          <div className={styles.imageWrapper}>
            <Img className={styles.image} src={image} />
          </div>
          <Button
            className={styles.buttonClose}
            dataTest={`${dataTest}__Button`}
            Icon={<Svg img={cross} size={1} />}
            onClick={onClose}
            variant="iconOnly"
          />
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default TipTile;
