import cx from 'classnames';
import React, { FC, Fragment } from 'react';

import Button from 'components/core/Button/Button';
import Svg from 'components/core/Svg/Svg';
import { cross } from 'svg/misc';

import styles from './Modal.module.scss';
import ModalProps from './types';

const Modal: FC<ModalProps> = ({
  className,
  children,
  header,
  Image,
  isOpen,
  isOverflowEnabled = true,
  isFullScreen,
  onClosePanel,
}) => (
  <Fragment>
    {isOverflowEnabled && (
      <div className={cx(styles.overflow, isOpen && styles.isOpen)} onClick={onClosePanel} />
    )}
    <div className={cx(styles.root, isOpen && styles.isOpen, className)}>
      {Image && <div className={styles.image}>{Image}</div>}
      <div className={cx(styles.body, Image && styles.hasImage)}>
        {header && <div className={styles.header}>{header}</div>}
        {children}
      </div>
      <Button
        className={cx(styles.buttonClose, isFullScreen && styles.isFullScreen)}
        Icon={<Svg img={cross} size={1} />}
        onClick={onClosePanel}
        variant="iconOnly"
      />
    </div>
  </Fragment>
);

export default Modal;
