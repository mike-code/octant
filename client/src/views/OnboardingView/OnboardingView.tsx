import React, { useState, useEffect, useCallback, ReactElement } from 'react';

import Img from 'components/core/Img/Img';
import Modal from 'components/core/Modal/Modal';
import ProgressStepperSlim from 'components/core/ProgressStepperSlim/ProgressStepperSlim';
import MainLayout from 'layouts/MainLayout/MainLayout';
import useOnboardingStore from 'store/onboarding/store';

import styles from './OnboardingView.module.scss';
import steps from './steps';

const OnboardingView = (): ReactElement => {
  const { setIsOnboardingDone } = useOnboardingStore();
  const [currentStepIndex, setCurrentStepIndex] = useState<number>(0);
  const currentStep = steps[currentStepIndex];

  const onOnboardingExit = useCallback(() => {
    setIsOnboardingDone(true);
  }, [setIsOnboardingDone]);

  useEffect(() => {
    if (currentStepIndex === steps.length) {
      onOnboardingExit();
    }
  }, [currentStepIndex, onOnboardingExit]);

  if (currentStepIndex === steps.length) {
    return <div />;
  }

  return (
    <MainLayout isHeaderVisible={false} isNavigationVisible={false}>
      <Modal
        header={currentStep.header}
        Image={<Img className={styles.image} src={currentStep.image} />}
        isFullScreen
        isOpen
        onClosePanel={onOnboardingExit}
      >
        <div className={styles.text}>{currentStep.text}</div>
        <ProgressStepperSlim
          className={styles.progressBar}
          currentStepIndex={currentStepIndex}
          numberOfSteps={steps.length}
          onStepClick={stepIndex => {
            if (stepIndex === currentStepIndex) {
              setCurrentStepIndex(stepIndex + 1);
              return;
            }
            setCurrentStepIndex(stepIndex);
          }}
        />
      </Modal>
    </MainLayout>
  );
};

export default OnboardingView;
