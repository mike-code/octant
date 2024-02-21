import { visitWithLoader, mockCoinPricesServer } from 'cypress/utils/e2e';
import viewports from 'cypress/utils/viewports';
import { IS_ONBOARDING_ALWAYS_VISIBLE, IS_ONBOARDING_DONE } from 'src/constants/localStorageKeys';
import { ROOT_ROUTES } from 'src/routes/RootRoutes/routes';

import Chainable = Cypress.Chainable;

const connectWallet = (): Chainable => {
  cy.intercept('GET', '/user/*/tos', { body: { accepted: true } });
  cy.get('[data-test=MainLayout__Button--connect]').click();
  cy.get('[data-test=ConnectWallet__BoxRounded--browserWallet]').click();
  cy.acceptMetamaskAccess();
  return cy.switchToCypressWindow();
};

Object.values(viewports).forEach(({ device, viewportWidth, viewportHeight }) => {
  describe(`earn: ${device}`, { viewportHeight, viewportWidth }, () => {
    before(() => {
      /**
       * Global Metamask setup done by Synpress is not always done.
       * Since Synpress needs to have valid provider to fetch the data from contracts,
       * setupMetamask is required in each test suite.
       */
      cy.setupMetamask();
    });

    beforeEach(() => {
      cy.disconnectMetamaskWalletFromAllDapps();
      mockCoinPricesServer();
      localStorage.setItem(IS_ONBOARDING_ALWAYS_VISIBLE, 'false');
      localStorage.setItem(IS_ONBOARDING_DONE, 'true');
      visitWithLoader(ROOT_ROUTES.earn.absolute);
    });

    // Disabled until flat gas is set in local chain (problem with high gas notification during first transaction)

    it('Wallet connected: Lock 1 GLM', () => {
      connectWallet();

      cy.get('[data-test=BoxGlmLock__Button]').click();
      cy.get('[data-test=BudgetBox__currentlyLocked__value]')
        .invoke('text')
        .then(text => {
          const amountToLock = 1;
          const lockedGlms = parseInt(text, 10);

          cy.get('[data-test=InputsCryptoFiat__InputText--crypto]').clear().type(`${amountToLock}`);
          cy.get('[data-test=GlmLockTabs__Button]').should('have.text', 'Lock');
          cy.get('[data-test=GlmLockTabs__Button]').click();
          cy.get('[data-test=GlmLockTabs__Button]').should('have.text', 'Waiting for confirmation');
          cy.confirmMetamaskPermissionToSpend();
          cy.get('[data-test=GlmLockTabs__Button]', { timeout: 180000 }).should(
            'have.text',
            'Close',
          );
          cy.get('[data-test=GlmLockNotification--success]').should('be.visible');
          cy.get('[data-test=GlmLockTabs__Button]').click();
          cy.get(
            '[data-test=BoxGlmLock__Section--current__DoubleValue__DoubleValueSkeleton]',
          ).should('be.visible');
          cy.get('[data-test=BoxGlmLock__Section--current__DoubleValue__primary]', {
            timeout: 60000,
          })
            .invoke('text')
            .then(nextText => {
              const lockedGlmsAfterLock = parseInt(nextText, 10);
              expect(lockedGlms + amountToLock).to.be.eq(lockedGlmsAfterLock);
            });
          cy.get('[data-test=HistoryItem__title]').first().should('have.text', 'Locked GLM');
          cy.get('[data-test=HistoryItem__DoubleValue__primary]')
            .first()
            .should('have.text', '1 GLM');
        });
    });

    it('Wallet connected: Unlock 1 GLM', () => {
      connectWallet();

      cy.get('[data-test=BoxGlmLock__Button]').click();
      cy.get('[data-test=BudgetBox__currentlyLocked__value]')
        .invoke('text')
        .then(text => {
          const amountToUnlock = 1;
          const lockedGlms = parseInt(text, 10);

          cy.get('[data-test=BoxRounded__tab--1]').click();
          cy.get('[data-test=InputsCryptoFiat__InputText--crypto]')
            .clear()
            .type(`${amountToUnlock}`);
          cy.get('[data-test=GlmLockTabs__Button]').should('have.text', 'Unlock');
          cy.get('[data-test=GlmLockTabs__Button]').click();
          cy.get('[data-test=GlmLockTabs__Button]').should('have.text', 'Waiting for confirmation');
          cy.confirmMetamaskPermissionToSpend();
          cy.get('[data-test=GlmLockTabs__Button]', { timeout: 60000 }).should(
            'have.text',
            'Close',
          );
          cy.get('[data-test=GlmLockNotification--success]').should('be.visible');
          cy.get('[data-test=GlmLockTabs__Button]').click();
          cy.get(
            '[data-test=BoxGlmLock__Section--current__DoubleValue__DoubleValueSkeleton]',
          ).should('be.visible');
          cy.get('[data-test=BoxGlmLock__Section--current__DoubleValue__primary]', {
            timeout: 60000,
          })
            .invoke('text')
            .then(nextText => {
              const lockedGlmsAfterUnlock = parseInt(nextText, 10);
              expect(lockedGlms - amountToUnlock).to.be.eq(lockedGlmsAfterUnlock);
            });
          cy.get('[data-test=HistoryItem__title]').first().should('have.text', 'Unlocked GLM');
          cy.get('[data-test=HistoryItem__DoubleValue__primary]')
            .first()
            .should('have.text', '1 GLM');
        });
    });
  });
});